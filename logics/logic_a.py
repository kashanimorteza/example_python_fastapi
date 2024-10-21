# logics/logic_a.py

from models.model_a import model_a 

class logic_a:

   #-------------------------- [List]
    def list(self):
        #--------------Description
        # IN     : 
        # OUT    : List of items
        # Action : Get all items

        #--------------Variable
        items = []
        
        #--------------Action
        item_1 = model_a(id=1, name='model_a_1')
        item_2 = model_a(id=2, name='model_a_2')
        items.append(item_1)
        items.append(item_2)

        #----------Return
        return items
    
   #-------------------------- [Item]
    def item(self, id: int):
        #--------------Description
        # IN     : Id
        # OUT    : model
        # Action : Get item based on id

        #--------------Variable
        
        #--------------Action
        model = model_a(id=id, name=f'model_a_{id}')

        #----------Return
        return model

   #-------------------------- [Add]
    def add(self, model : model_a):
        #--------------Description
        # IN     : model
        # OUT    : True / False
        # Action : Add item

        #--------------Variable
        output = True

        #--------------Action
        print(f"Item added : {model.id}")

        #----------Return
        return output
    
   #-------------------------- [Edit]
    def edit(self, model : model_a):
        #--------------Description
        # IN     : model
        # OUT    : True / False
        # Action : Edit item

        #--------------Variable
        output = True

        #--------------Action
        print(f"Item edited : {model.id}")

        #----------Return
        return output
    
   #-------------------------- [Delete]
    def delete(self, id : int):
        #--------------Description
        # IN     : id
        # OUT    : True / False
        # Action : Delete item based on id

        #--------------Variable
        output = True

        #--------------Action
        print(f"Item deleted : {id}")
        
        #----------Return
        return output
