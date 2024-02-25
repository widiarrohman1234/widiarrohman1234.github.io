# Catatan Node.js

> catan ini masih temporary, dicatan jika ada masalah/kendala.

## import dan export module
```
// ./function.js
const homePage = async () => {
    console.log('Ini halaman homePage')
}

const detailPage = async () => {
    console.log('Ini halaman detailPage')
}

module.exports = {homePage, detailPage}
```

```
// ./running.js
const {homePage, detailPage} = require("./function.js")
homePage()
detailPage()
```