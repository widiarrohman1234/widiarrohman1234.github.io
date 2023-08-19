# Dokumentasi React.js

## Instalasi
```
npx create-react-app fe-react-lelang
```

- `npm start` : Starts the development server.
- `npm run build` : Bundles the app into static files for production.
- `npm test` : Starts the test runner.
- `npm run eject` : Removes this tool and copies build dependencies, configuration files and scripts into the app directory. If you do this, you can’t go back!

## Struktur Folder
```
my-react-app/
|-- public/
|   |-- index.html
|   |-- ...
|-- src/
|   |-- assets/
|   |   |-- images/
|   |   |-- styles/
|   |-- components/
|   |   |-- Header/
|   |   |   |-- Header.js
|   |   |   |-- Header.css
|   |-- pages/
|   |   |-- Home/
|   |   |   |-- Home.js
|   |   |   |-- Home.css
|   |   |-- About/
|   |   |   |-- About.js
|   |   |   |-- About.css
|   |-- App.js
|   |-- index.js
|-- package.json
|-- README.md
|-- ...

```

## React Router DOM
```
npm install react-router-dom
```
contoh penggunaan
```
// Home.js
import React from 'react';

function Home() {
  return <h1>Halaman Beranda</h1>;
}

export default Home;
```
```
// About.js
import React from 'react';

function About() {
  return <h1>Tentang Kami</h1>;
}

export default About;
```
```
import logo from "./logo.svg";
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import "./App.css";
import Home from "./Home";
import About from './About';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>Selamat datang di Scrapping lelang.go.id</p>
          <h4>Yuk, lihat fitur keren didalamnya</h4>
          <nav>
            <ul>
              <li>
                <Link to="/">Beranda</Link>
              </li>
              <li>
                <Link to="/about">Tentang</Link>
              </li>
            </ul>
          </nav>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </header>
      </div>
    </Router>
  );
}

export default App;

```

## Core concepts
3 hal yang wajib dikuasai pada pembelajaran React.js
1. components
- dibuat menggunanakan function
- nama function diawali huruf besar
- mereturn element UI
2. props
3. state

