let express = require("express");
let path = require("path");
let app = express();
let session = require("express-session");
const bcrypt = require("bcrypt");

// config view engine setup ejs
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// middleware
app.use(express.urlencoded({ extended: false }));
app.use(
  session({
    resave: false, // don't save session if unmodified
    saveUninitialized: false, // don't create session until something stored
    secret: "shhhh, very secret",
  })
);

// Session-persisted message middleware
app.use(function (req, res, next) {
  let err = req.session.error;
  let msg = req.session.success;
  delete req.session.error;
  delete req.session.success;
  res.locals.message = "";
  if (err) res.locals.message = '<p class="msg error">' + err + "</p>";
  if (msg) res.locals.message = '<p class="msg success">' + msg + "</p>";
  next();
});

// Dummy database
let users = {
  tj: {
    name: "tj",
  },
};

// Function to hash a password and generate a salt
function hash(password, callback) {
  const saltRounds = 10; // The number of salt rounds

  bcrypt.genSalt(saltRounds, function (err, salt) {
    if (err) {
      return callback(err);
    }

    bcrypt.hash(password, salt, function (err, hash) {
      if (err) {
        return callback(err);
      }

      // Now, you have the salt and hash, pass them to the callback.
      callback(null, password, salt, hash);
    });
  });
}

// Usage example
hash("foobar", function (err, pass, salt, hash) {
  if (err) {
    throw err;
  }

  // Store the salt and hash in the "db"
  users.tj.salt = salt;
  users.tj.hash = hash;
  console.log("users:", users);
});

// Authenticate using our plain-object database of doom!
function authenticate(name, pass, fn) {
  if (!module.parent) console.log("authenticating %s:%s", name, pass);
  let user = users[name];
  if (!user) return fn(null, null);
  bcrypt.compare(pass, user.hash, function (err, res) {
    if (res) {
      return fn(null, user);
    }
    fn(null, null);
  });
}

function restrict(req, res, next) {
  if (req.session.user) {
    next();
  } else {
    req.session.error = "Access denied!";
    res.redirect("/login");
  }
}
app.get("/", function (req, res) {
  res.redirect("/login");
});

app.get("/restricted", restrict, function (req, res) {
  res.send('Wahoo! restricted area, click to <a href="/logout">logout</a>');
});

app.get("/logout", function (req, res) {
  // destroy the user's session to log them out
  // will be re-created next request
  req.session.destroy(function () {
    res.redirect("/");
  });
});

app.get("/login", function (req, res) {
  res.render("login");
});

app.post("/login", function (req, res, next) {
  authenticate(req.body.username, req.body.password, function (err, user) {
    if (err) return next(err);
    if (user) {
      req.session.regenerate(function () {
        req.session.user = user;
        req.session.success =
          "Authenticated as " +
          user.name +
          ' click to <a href="/logout">logout</a>. ' +
          ' You may now access <a href="/restricted">/restricted</a>.';
        res.redirect("back");
      });
    } else {
      req.session.error =
        "Authentication failed, please check your " + "username and password.";
      res.redirect("/login");
    }
  });
});


/* istanbul ignore next */
if (!module.parent) {
  app.listen(3000);
  console.log("Express started on port 3000");
}

module.exports = app;
