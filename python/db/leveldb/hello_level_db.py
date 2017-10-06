import leveldb

db = leveldb.LevelDB("./sample.db")
db.Put("hello", "world")

print db.Get("hello")
print dir(db)
