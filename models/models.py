from flask_sqlalchemy import SQLAlchemy                                                                                                                                                          
from sqlalchemy import Column,Integer,String,ForeignKey,Date,DateTime,BLOB
from sqlalchemy.orm import relationship                                                                                                                                                          
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db=SQLAlchemy() 

class Usuarios(db.Model):
    __tablename__ = "Usuarios"
    Id_Usuario=Column(Integer,primary_key=True)
    nombre=Column(Integer,nullable=False)
    passwd=Column(String,nullable=False)

    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        user=self.query.all()                                                                                                                                                                   
        return pago
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        pago=self.consultaIndividual()
        db.session.delete(pago)
        db.session.commit()
    def consultaIndividual(self):
        pago=self.query.get(self.Id_Usuario)
        return pago
    
    