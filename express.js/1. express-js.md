# Catatan belajar Express-js

## 1. Start

## 2. Routing method
![routing-method-express-js](./image/routing-method-express-js.png)

- hello world
```
const express = require("express")

const app = express()
const port = 3000

app.get('/',(req, res)=>{
    // res.send(`hello world`)
    res.status(200).json({name: "john"})
})

app.listen(port,()=> {
    console.log(`server listen on port ${port}`)
})
```

## 3. Express application generator
```
npx express-generator
```

```
npm install
```

```
SET DEBUG=express-learn:* & npm start
```

![directory-struktur](./image/directory-struktur.png)

- load [http://localhost:3000/](http://localhost:3000/)

## 4. Basic routing 

> app.**METHOD**(PATH, HANDLER)

```
app.get("/", (req, res) => {
  res.send(`Hello World`);
  //   res.status(200).json({ name: "john" });
});

app.post("/", (req, res) => {
  res.send("got a post request");
});

app.put("/user", (req, res) => {
  res.send("got a put request /user");
});

app.delete("/user", (req, res) => {
  res.send("Got a DELETE request at /user");
});
```

## 5. Request URL
![request URL](./image/request-url.png)
```
app.get("/hostname", (req, res) => {
  res.send({
    hostname: req.hostname,
    path: req.path,
    originalUrl: req.originalUrl,
    protocol: req.protocol,
    secure: req.secure,
    subdomains: req.subdomains
  });
});
```
## 6. Request query param
[http://localhost:3000/user/12/ops/wira](http://localhost:3000/user/12/ops/wira)
```
app.get("/admin/:id/:role/:username", (req, res) => {
  res.send({
    id: req.params.id,
    role: req.params.role,
    username: req.params.username,
  });
});
```

## 7.
## 8.
## 9.
## 10.
## 11.
## 12.
















