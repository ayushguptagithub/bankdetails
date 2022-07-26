from fastapi import FastAPI, Depends
import schemas
import models
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 

Base.metadata.create_all(engine)

# separate session for each request so this function will be called for every request
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


@app.get("/openings")
async def getItems(db:Session=Depends(db_session)):
    openings = db.query(models.Item).all()
    return openings


@app.get("find/{bank_id}")#path parameter 
async def getItem(bank_id:int, db: Session=Depends(db_session)):
    item = db.query(models.Item).get(bank_id)
    return item


@app.post("/Add/{bank_id}")
async def addItem(item:schemas.Item, db:Session=Depends(db_session)):
    item = models.Item(user_id = item.user_id, acc_no= item.acc_no, ifcr_no=item.ifcr_no,micr_no=item.micr_no,swift=item.swift )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item 

@app.put("/update/{bank_id}")
async def updateItem(bank_id:int, item:schemas.Item, db: Session = Depends(db_session)):
    itemObject = db.query(models.Item).get(bank_id)
   # itemObject.task = item.task
    itemObject.user_id = item.user_id
    itemObject.acc_no= item.acc_no 
    itemObject.ifcr_no=item.ifcr_no
    itemObject.micr_no=item.micr_no
    itemObject.swift=item.swift 
    db.commit()
    return itemObject
   
@app.delete("/{bank_id}")
async def deleteItem(bank_id:int, db:Session= Depends(db_session)):
    itemObject = db.query(models.Item).get(bank_id)
    db.delete(itemObject)
    db.commit()
    db.close()
    return {' deleted...{bank_id} succesfully'}

