from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from database import engine,SessionLocal
import models
from schema import PersonResponse,PersonQuery,PersonCreate
models.Base.metadata.create_all(bind=engine)

app=FastAPI()


@app.get('/')
def say_hello():
    return {"res":"hello yo"}

@app.get('/api')
def get_all_persons(db:Session=Depends(get_db)):
    persons=db.query(models.Person).all()
    return {"persons":persons}

@app.post('/api')
def create_person(person:PersonCreate,db:Session=Depends(get_db)):
    new_person=models.Person(name=person.name)
    db.add(new_person)
    db.commit()
    db.refresh(new_person)

    return new_person

@app.get('/api/{pk}')
def get_user(pk:int,db:Session=Depends(get_db)):
    person=db.query(models.Person).filter(models.Person.id==pk).first()

    if person is None:
            raise HTTPException(404,detail={
            "not found":"person not found"
        })

    else:
        return person

@app.delete('/api/{pk}')
def delete_person(pk:int,db:Session=Depends(get_db)):
    person=db.query(models.Person).filter(models.Person.id==pk)
    if person is None:
            raise HTTPException(404,detail={
            "not found":"person not found"
        })
    else:
        person.delete(synchronize_session=False)
        db.commit()
        return {"deleted":"school removed"}


@app.put('/api/{pk}')
def update_person(pk:int,data:PersonCreate,db:Session=Depends(get_db)):
    person=db.query(models.Person).filter(models.Person.id==pk)
    if person is None:
            raise HTTPException(404,detail={
            "not found":"person not found"
        })
    else:
        person.update(data.dict(),synchronize_session=False)
        db.commit()
        return {"updated":person.first()}


