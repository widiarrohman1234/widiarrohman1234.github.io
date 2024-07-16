## Database
use belajar
db.dropDatabase()
db.getName()
db.hostInfo()
db.version()
db.stats()

## Collection
max 16mb/document
max level nested 100 level
db.getCollectionNames()
db.createCollection(name)
db.getCollection(name)
db.getCollectionInfos()

db.collection.find()
db.collection.count()
db.collection.drop()
db.collection.totalSize()
db.collection.stats()

ex:
db.createCollection("products")
db.createCollection("customers")
db.createCollection("orders")

## Data Model
embedded
reference

## BSON (Binary JSON)
tipe data | alias
double | double
string | string
object | object
array | array
binary data | binData
objectId | objectId
boolean | bool
date | date
null | null
regular expression | regex
javascript | javascript
32 bit integer | int
64 bit integer | long
timestamp | timestamp
decimal 128 | decimal

- objectId= random data uniq 12 byte (4 byte timestamp, 5 random value, 3 increment counter)
- date=64bit integer unix epoch (1 jan 1970 00.00.00)

## Insert Document
new ObjectId()
db.collection.insertOne(document)
db.collection.insertMany(array`[document])
ex:
db.customers.insertOne({
    _id: new ObjectId(),
    name: "John Doe",
})
db.products.insertMany([
    {
        _id: new ObjectId(),
        name: "Laptop",
        price: 1000,
    },
    {
        _id: new ObjectId(),
        name: "Mouse",
        price: 20,
    },
])
db.orders.insertOne({
    _id: new ObjectId(),
    total: new NumberLong("12000"),
    items: [
        {
            productId: ObjectId("65fb0a4a384866759e5dcf67"),
            price: new NumberLong(5000),
            quantity: 2,
        },
        {
            productId: ObjectId("65fb0a4a384866759e5dcf68"),
            price: new NumberLong(7000),
            quantity: 1,
        },
    ],
})

## Query Document
db.collection.find(query)
ex:
select * from customers where _id=ObjectId("65fb0a4a384866759e5dcf68")
db.customers.find({_id: ObjectId("65fb0a3f384866759e5dcf66")})

select * from customers where name="John Doe"
db.customers.find({name: "John Doe"})

select * from products where price=5000
db.products.find({price: 1000})

select * from orders where items.productId=ObjectId("65fb0a4a384866759e5dcf68")
db.orders.find({"items.productId": ObjectId("65fb0a4a384866759e5dcf68")})

## Comaparison Query Operator
- $eq (equal) =
- $gt (greater than) >
- $gte (greater than or equal) >=
- $lt (less than) <
- $lte (less than or equal) <=
- $in (in) in
- $nin (not in) not in
- $ne (not equal) !=
  
ex:
select * from products where price=1000
db.products.find({price: {$eq: 1000}})

select * from products where price>800
db.products.find({price: {$gt: 800}})

select * from products where price>=1000
db.products.find({price: {$gte: 1000}})

select * from products where price<1000
db.products.find({price: {$lt: 1000}})

select * from products where price<=1000
db.products.find({price: {$lte: 1000}})

select * from products where price in (1000, 2000, 3000)
db.products.find({price: {$in: [1000, 2000, 3000]}})

select * from products where price not in (1000, 2000, 3000)
db.products.find({price: {$nin: [1000, 2000, 3000]}})

select * from products where price!=1000 and name="Laptop"
db.products.find({price: {$ne: 1000}, name: "Laptop"})


## Logical Query Operator
- $and (and) and
- $or (or) or
- $nor (nor) nor
- $not (not) not

ex:
select * from products where price=1000 and name="Laptop"
db.products.find({$and: [{price: 1000}, {name: "Laptop"}]})

select * from products where price=1000 or name="Mouse"
db.products.find({$or: [{price: 1000}, {name: "Mouse"}]})

select * from products where price!=1000
db.products.find({$nor: [{price: 1000}]})

select * from products where price!=1000
db.products.find({price: {$not: {$eq: 1000}}})

## Element Query Operator
- $exists (exists) exists
- $type (type) type
- $mod (mod) mod
- $regex (regex) regex
- $text (text) text
- $where (where) where
- $comment (comment) comment
- $jsonSchema (jsonSchema) jsonSchema
- $geoIntersects (geoIntersects) geoIntersects
- $geoWithin (geoWithin) geoWithin
- $near (near) near
- $nearSphere (nearSphere) nearSphere
- $all (all) all
- $elemMatch (elemMatch) elemMatch
- $size (size) size
- $bitsAllClear (bitsAllClear) bitsAllClear
- $bitsAllSet (bitsAllSet) bitsAllSet
- $bitsAnyClear (bitsAnyClear) bitsAnyClear
- $bitsAnySet (bitsAnySet) bitsAnySet
- $elemMatch (elemMatch) elemMatch

ex:
select * from products where price exists
db.products.find({price: {$exists: true}})

select * from products where price not exists
db.products.find({price: {$exists: false}})

select * from products where price is string
db.products.find({price: {$type: "string"}})

select * from products where price is number
db.products.find({price: {$type: "number"}}})

select * from products where price is array
db.products.find({price: {$type: "array"}}})

select * from products where price is object
db.products.find({price: {$type: "object"}}})

select * from products where price is boolean
db.products.find({price: {$type: "boolean"}}})

select * from products where price is null
db.products.find({price: {$type: "null"}})

select * from products where price is javascript
db.products.find({price: {$type: "javascript"}}})

## Evaluation Query Operator
- $expr (expr) aggregation operator
- $jsonSchema (jsonSchema) jsonSchema https://json-schema.org/
- $mod (mod) modulo
- $regex (regex) mengambil data dengan regex %like%
- $text (text) mengambil data dengan text
- $where (where) mengambil data dengan javascript

ex:

mod: select * from products where price%2=0
db.products.find({$expr: {$mod: ["$price", 2]}})

regex: select * from products where name like "%Lap%"
db.products.find({name: {$regex: /Lap/}})
regex: select * from products where name like "Lap%"
db.products.find({name: {$regex: /^Lap/}})
regex: select * from products where name like "%top"
db.products.find({name: {$regex: /top$/}})

jsonSchema: select * from products where name is string and price is number
db.products.find({
    $jsonSchema:{
        required: ["name", "price"],
        type: "object",
        properties: {
            name: {type: "string"},
            price: {type: "number"},
        },
    }
})

where: select * from products where _id=ObjectId("65fb0a4a384866759e5dcf67")
note: gunakan mongo shell, tidak bisa di compass
db.products.find({$where: function(){
    return this._id.str === "65fb0a4a384866759e5dcf67"
}})

## Array Query Operator
- $all (all) mencocokkan array yang mengandung element-element tertentu
- $elemMatch (elemMatch) mencocokkan array yang mengandung element yang memenuhi kondisi tertentu
- $size (size) mengambil document dengan jumlah size array tertentu

db.products.insertMany([
    {
        name: "Laptop",
        price: 1000,
        category: "electronics",
        tags: ["electronics", "laptop", "computer"],
    },{
        name: "Mouse",
        price: 20,
        category: "electronics",
        tags: ["electronics", "mouse", "computer"],
    },{
        name: "T-Shirt",
        price: 10,
        category: "clothes",
        tags: ["clothes", "t-shirt"],
    }
])

ex:
select * from products where tags contains "electronics" and "laptop"
db.products.find({tags: {$all: ["electronics", "laptop"]}})

elemMatch eq: select * from products where tags contains "mouse" and "clothes"
db.products.find({tags: {$elemMatch: {$eq: "mouse", $eq: "clothes"}}})

elemMatch in: select * from products where tags contains "electronics" or "clothes"
db.products.find({tags: {$elemMatch: {$in: ["electronics", "clothes"]}}})

size: select * from products where tags size 2
db.products.find({tags: {$size: 2}})

## Projection Operator
db.collection.find(query, projection)

ex:
select name from products
db.products.find({}, {name: 1, _id: 0})

select name, price from products
db.products.find({}, {name: 1, price: 1, _id: 0})

select name, price from products where price=1000
db.products.find({price: 1000}, {name: 1, price: 1, _id: 0})

### Projection Operator
- 1: include
- 0: exclude
- $: limit array hanya mengembalikan satu element
- $elemMatch: limit array hanya mengembalikan satu element yang memenuhi kondisi tertentu
- $meta: mengekstrak metadata dari matching document
- $slice: mengambil sebagian element dari array

ex:
$: ambil satu element yang ada tags 
db.products.find({
    tags:{
        $exists: true,
    }
}, {
    name: 1,
    "tags.$": 1,
})

$: ambil 2 terdepan dari tags
db.products.find({
    tags:{
        $exists: true,
    }
}, {
    name: 1,
    tags: {
        $slice: 2,
    },
})

$meta: cooming soon

## Query Modifiers
- count: menghitung jumlah document yang terpilih
- limit(size): membatasi jumlah document yang terpilih
- skip(size): melewati sejumlah document yang terpilih
- sort(query): mengurutkan document yang terpilih
note: 1=asc, 0=desc

ex:
select count(*) from products
db.products.find().count()

select * from products limit 2
db.products.find().limit(2)

select * from products limit 2 offset 1
db.products.find().limit(2).skip(1)

select * from products order by name asc
db.products.find().sort({name: 1})

select * from products order by name desc, price asc
db.products.find().sort({name: -1, price: 1})

// order by name desc, price asc and limit offset
db.products.find().sort({name: -1, price: 1}).limit(2).skip(1)

## UPDATE Document
- updateOne(query, update) : update satu document
- updateMany(query, update) : update banyak document
- replaceOne(query, replacement) : replace satu document
db.collection.updateOne(
    {}, // filter
    {}, // update
    {} // options
)
db.collection.updateMany(
    {}, // filter
    {}, // update
    {} // options
)
db.collection.replaceOne(
    {}, // filter
    {} // replacement
)

ex:
updateOne: update price=7000 where name="T-Shirt"
db.products.updateOne({name: "T-Shirt"}, {$set: {price: 7000}})

updateMany: update product set tags=["clothes", "t-shirt"] where name="T-Shirt" and price=7000
db.products.updateMany({name: "T-Shirt", price: 7000}, {$set: {tags: ["kaos", "t-shirt"]}})

replaceOne: replace product where name="T-Shirt" and price=7000
db.products.replaceOne({name: "T-Shirt", price: 7000}, {
    name: "Kaos",
    price: 7000,
    category: "clothes",
    tags: ["clothes", "t-shirt"],
})

## Field update operator
- $set: mengubah nilai field document
- $unset: menghapus field document
- $rename: mengubah nama field
- $inc: menambahkan nilai field
- $currentDate: mengubah nilai field menjadi tanggal sekarang

ex:
$set: update product set stock=10
db.products.updateMany({}, {$set: {stock: 0}})

$inc: update product set stock=stock+10
db.products.updateMany({}, {$inc: {stock: 10}})

$rename: alter table products rename column name to title
db.products.updateMany({}, {$rename: {name: "title"}})

$unset: alter table products drop column stock
db.products.updateMany({}, {$unset: {stock: ""}})

$currentDate: update product set lastUpdated=now()
db.products.updateMany({}, {$currentDate: {lastUpdated: true}})

## Array update operator
- $ : update array ke n
- $[] : update semua array
- $[<identifier>] : update array dengan identifier tertentu
- <index>: update array dengan index tertentu
- $addToSet: menambahkan element ke array jika belum ada
- $pop: menghapus element pertama (-1) atau terakhir (1) dari array
- $pull: menghapus element dari array sesuai kondisi
- $push: menambahkan element ke array
- $pullAll: menghapus element yang ada di array

ex:
$: update product set ratings=[90, 85, 80]
db.products.updateMany({}, {$set: {ratings: [90, 85, 80]}})

$[]: update product set ratings=[100]
db.products.updateMany({
    ratings: 100
}, {$set: {"ratings.$": 60}})

$[]: update product set ratings=[100, 100, 100]
db.products.updateMany({}, {$set: {"ratings.$[]": 100}})

$[<identifier>]: update product set ratings=[100, 85, 80]
db.products.updateMany({
    ratings: 90
}, {$set: {"ratings.$[element]": 100}}, {
    arrayFilters: [{element: {$gte:85}}]
})

<index>: update product set ratings=[90, 85, 100]
db.products.updateMany({}, {$set: {"ratings.1":97,"ratings.2": 80}})

addToSet: update product set tags=["clothes", "t-shirt", "kaos"]
db.products.updateMany({_id: ObjectId("65fb14aec87b1634c2ac134c")}, {$addToSet: {tags: "celana"}})

pop: update product 
db.products.updateMany({_id:ObjectId("65fb14aec87b1634c2ac134c")},{$pop:{ratings:1}}) // remove last
db.products.updateMany({_id:ObjectId("65fb14aec87b1634c2ac134c")},{$pop:{ratings:-1}}) // remove first

pull: update product set ratings=[90, 85]
db.products.updateMany({}, {$pull: {ratings: {$gte: 85}}})

push: update product set ratings=[90, 85, 80, 100]
db.products.updateMany({}, {$push: {ratings: 100}})

pullAll: hapus nilai 100 dan 0 dari ratings
db.products.updateMany({},{$pullAll:{ratings: [100,0]}})

### Array update operator modifier
- $each: digunakan $addToSet dan $push, menambahkan multiple element ke array
- $position: digunakan $push, menambahkan element ke posisi tertentu
- $slice: digunakan $push, membatasi jumlah element array
- $sort: digunakan $push, mengurutkan element array

ex:
$each: update product set ratings=[100,200,300,80]
db.products.updateMany({_id: ObjectId("65fb14aec87b1634c2ac134c")},{$push:{ratings:{$each:[100,200,300,80]}}} )
$each addToSet
db.products.updateMany({_id:ObjectId("65fb14aec87b1634c2ac134c")},{$addToSet:{tags:{$each:["kaos","jam"]}}})
$each push index
db.products.updateMany({_id:ObjectId("65fb14aec87b1634c2ac134c")},{$push:{tags:{$each:["jubah"], $position: 5}}})
$each push sorting
db.products.updateMany({_id:ObjectId("65fb14aec87b1634c2ac134c")},{$push:{tags:{$each:["jubah"], $sort: 1}}})
db.products.updateMany({_id:ObjectId("65fb14aec87b1634c2ac134c")},{$push:{ratings:{$each:[100,200,300,80], $sort: 1}}})
$each push slice
db.products.updateMany({_id:ObjectId("65fb14aec87b1634c2ac134c")},{$push:{ratings:{$each:[100,200,300,80], $slice: 5}}}) // slice 5 belakang
db.products.updateMany({_id:ObjectId("65fb14aec87b1634c2ac134c")},{$push:{ratings:{$each:[100,200,300,80], $slice: -5}}}) // slice 5 depan
$each push slice sort
db.products.updateMany({_id:ObjectId("65fb14aec87b1634c2ac134c")},{$push:{ratings:{$each:[100,200,300,80], $slice: 5, $sort: 1}}}) // slice 5 belakang dan sort asc

## Delete Document
- db.collection.deleteOne(query) : delete satu document
- db.collection.deleteMany(query) : delete banyak document

ex:
db.customers.insertOne({_id:"spammer", name:"Spammer"})
db.customers.deleteOne({_id: "spammer"})

db.customers.insertOne({_id:"spammer1", name:"Spammer1"})
db.customers.insertOne({_id:"spammer2", name:"Spammer2"})
db.customers.insertOne({_id:"spammer3", name:"Spammer3"})
db.customers.deleteMany({_id:{$regex: "spammer"}})

## Bulk Write Operation
- db.collection.bulkWrite([operation1, operation2, ...])
- db.collection.insertMany([{document1}, {document2}, ...])
- db.collection.updateMany([{filter1, update1}, {filter2, update2}, ...])
- db.collection.deleteMany([{filter1}, {filter2}, ...])
- db.collection.replaceOne([{filter1, replacement1}, {filter2, replacement2}, ...])
ex:
db.customers.bulkWrite([
    {
        insertOne: {
            document: {
                _id: "spammer1",
                name: "Spammer1",
            }
        }
    },
    {
        insertOne: {
            document: {
                _id: "spammer2",
                name: "Spammer2",
            }
        }
    },
    {
        insertOne: {
            document: {
                _id: "spammer3",
                name: "Spammer3",
            }
        }
    },
    {
        deleteOne: {
            filter: {
                _id: {$regex: "spammer"}
            }
        }
    }
])

## Indexes
BTREE (Binary Tree)
1=asc,-1=desc

- db.collection.getIndexes()
- db.collection.createIndex(keys, options)
- db.collection.dropIndex(index)

ex:
db.products.getIndexes()
db.products.createIndex({
    price: 1,
})
db.products.getIndexes()
db.products.find({
    price: 1000,
}).explain()
db.products.find({
    name:"Laptop",
}).explain()

db.products.dropIndex("price_1")

### Compound Indexes
index lebih dari 1, max 32 index dalam 1 collection
db.products.createIndex({
    price: 1,
    name: 1,
})
db.products.find({
    price: 1000,
    name: "Laptop",
}).explain()

db.products.find({
    price: 1000,
}).explain()

## Text Indexes
mencari text dalam document atau array
- db.collection.createIndex({field: "text"})
- db.collection.find({$text: {$search: "text"}})

ex:
db.products.createIndex({
    name: "text",
    category: "text",
}, {
    default_language: "english",
    language_override: "language",
    weights: {
        title: 10,
        category: 5,
    }
})
// mencari "Laptop"
db.products.find({
    $text: {
        $search: "Laptop",
    }
})

// mencari "Laptop" dan "Mouse"
db.products.find({
    $text: {
        $search: "Laptop Mouse",
    }
})

// mencari "mie sedap"
db.products.find({
    $text: {
        $search: '"mie sedap"',
    }
})

// mencari "mie" tanpa "sedap"
db.products.find({
    $text: {
        $search: "mie -sedap",
    }
})

### Meta operator
- $meta: "textScore"
ex:
db.products.find({
    $text: {
        $search: "Laptop",
    }
}, {
    score: {
        $meta: "textScore",
    }
})

## Wildcard Indexes
befungsi untuk memberikan index pada embedded document yang tidak diketahui
- db.collection.createIndex({field: 1})
- db.collection.createIndex({field: "text"})

ex:
// buat data
db.customers.insertMany([{
    _id: "customer1",
    name: "Customer 1",
    customFields: {
        hobby: "membaca",
        university: "Universitas",
    }
},{
    _id: "customer2",
    name: "Customer 2",
    customFields: {
        ipk: 3.4,
        university: "Politeknik",
    }
},{
    _id: "customer3",
    name: "Customer 3",
    customFields: {
        motherName: "Dila",
        passion: "enterpreneur",
    }
}])

// lakukan index
db.customers.createIndex({
    "customFields.$**": 1,
})

// cek index
db.customers.getIndexes()
db.customers.find({
    "customFields.hobby": "membaca",
}).explain()

## Index Properties
TTL (Time To Live) waktu untuk hidup
TTL index hanya digunakan field tipe data Date
data akan terhapus setelah 10 detik dari createdAt
contoh: createdAt 1 januari 2030, lewat 10 detik, data dihapus
db.createCollection("sessions")
db.sessions.insertOne({
    _id:1,
    createdAt: new Date()
})
db.sessions.createIndex({
    createdAt:1
}, {expireAfterSeconds: 10})

### Unique Index
membuat uniq index
note: 
sparse:true hanya diterapkan pada dokumen yang memiliki field yang di index
sparse:true mengizinkan field null sama dengan null
- createIndex({object},{unique:true,sparse:true})

ex:
db.customers.createIndex({
    email:1
},{
    unique: true,
    sparse:true
})

// update data
db.customers.updateOne({
    _id:"customer1"
},{
    $set:{
        email: "customer1@gmail.com"
    }
})

### Index Case Insensitive
// setting index agar insensitive
db.customers.createIndex({
    name:1
},{
    collation:{
        locale:"en",
        strength:2
    }
})
db.customers.insertOne({
    name:"john Doe"
})

// melakukan pencarian insensitive
db.customers.find({
    name:"john Doe"
}).collation({
    locale:"en",
    strength:2
})


### Partial Filter Index
melakukan index pada kondisi tertentu saja

// buat field stock
db.products.updateMany({}, {$set: {stock: 0}})

// pasang index partial
db.products.createIndex({
    price:1
},{
    partialFilterExpression:{
        stock:{
            $gt:0
        }
    }
})

// cek data
db.products.find({
    price:{
        $eq:1000
    },
     stock:{
        $gt:0
    }
}).explain()

## Security
- db.createUser

ex:
use admin
db.createUser({
    user: "mongo",
    pwd: "mongo",
    roles: [
        "readWriteAnyDatabase",
        "userAdminAnyDatabase",
    ]
})

"mongodb://mongo:mongo@localhost:27017/belajar?authSource=admin"

## User
- db.createUser()
- db.getUser()
- db.dropUser()
- db.updateUser()
- db.changeUserPassword()

database roles:
- read: read only
- readWrite: read and write
- dbAdmin: admin database
- userAdmin: membuat user dan role
- dbOwner: semua akses
- readAnyDatabase: read all database
- readWriteAnyDatabase: read and write all database
- userAdminAnyDatabase: membuat user dan role all database
- dbAdminAnyDatabase: admin database all database
- backup: backup
- restore: restore
- root: superuser
- clusterAdmin: admin cluster

ex:
use admin
// read
db.createUser({
    user: "read",
    pwd: "read",
    roles: [
        {role: "read", db: "belajar"},
    ]
})
// readWrite
db.createUser({
    user: "readWrite",
    pwd: "readWrite",
    roles: [
        {role: "readWrite", db: "belajar"},
    ]
})
// change password
db.changeUserPassword("readWrite", "readWrite1")
// get users
db.getUsers()
// drop user
db.dropUser("readWrite")
// update user
db.updateUser("read", {
    roles: [
        {role: "readWrite", db: "belajar"},
    ]
})

## Custom Role
- db.createRole()
- db.getRoles(): mengembalikan role yang sudah dibuat
- db.deleteRole()
- db.updateRole()

ex:
use admin
db.createRole({
    role: "session_management",
    roles: [{role: "read", db: "belajar"}],
    privileges: [
        {
            resource: {
                db: "belajar",
                collection: "sessions",
            },
            actions: ["find", "insert", "update", "remove"],
        }
    ],
})

// cek roles
db.getRoles()
// cek roles dan privileges
db.getRoles({showPrivileges: true})
// buat user dengan custom role
db.createUser({
    user: "customUser",
    pwd: "customUser",
    roles: ["session_management"],
})
// drop role
db.dropRole("session_management")
// update role
db.updateRole("session_management", {
    privileges: [
        {
            resource: {
                db: "belajar",
                collection: "sessions",
            },
            actions: ["find", "insert", "update", "remove"],
        }
    ],
})

## Backup
## Restore

























