#use to declare datatype 
from pydantic import BaseModel

#types
class Item(BaseModel):
   user_id:int
   acc_no:str
   ifcr_no:str
   micr_no:str
   swift:str

    

   