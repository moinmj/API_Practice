from pydantic import BaseModel, Field, field_validator,model_validator,computed_field #type:ignore
from typing import Optional,List
class User(BaseModel):
    id:int
    name:str
    is_active:bool

input_data= {"id":2,"name":"Moin","is_active":True}
user=User(**input_data)
print(user)
class Employee(BaseModel):
    id:int
    name:str=Field(...,min_length=3,max_length=50,description="Employee Name",example="Moin")
    department= Optional[str]="General"
    salary:float=Field(...,ge=10000)
class User1(BaseModel):
    username:str

    @field_validator("username")
    def username_length(cls,v):
        if len(v) <4:
            raise ValueError("username must be atleast four characters")
        return v
    
class signupdata(BaseModel):
    password:str
    confirm_password:str
    @model_validator(mode="after")
    def password_match(cls,values):
        if values.password != values.confirm_password:
            raise ValueError("Password do not match")
        return values
    class Product(BaseModel):
        price:float
        quantity:int

        @computed_field
        @property
        def total_price(self)->float:
            return self.price * self.quantity
class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class User2(BaseModel):
    id:int
    name:str
    address:Address #nested model refrencing,This class is reffering to class address
class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']]= None #self replication,self refrencing,--->forward refrencing--->when forward refrencing done we have to take that class in next line with a method model.rebuild
Comment.model_rebuild()

address= Address(
    street="123 something",
    city="Jaipur",
    postal_code="10110")
user23=User2(
    id=1,
    name="Moin",
    address=address
)
comments=Comment(
    id=1,
    content="First comment",
    replies=[
        Comment(id=2,content="reply1"),
        Comment(id=3,content="reply2"),

    ]
)
