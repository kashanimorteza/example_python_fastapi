# myLibs/lib_a.py


class lib_a:
    
    #-------------------------- [Init]
    def __init__(self):
        self.modoule = "lib_a"


   #-------------------------- [List]
    def list(self, params={}):
        #--------------Description
        # IN     : 
        # OUT    : Status / Data
        # Action : Items

        #--------------Variable
        output = {}
        output["status"] = True

        #--------------Action
        output['data'] = "list of model_a"

        #----------Return
        return output
    
   #-------------------------- [Item]
    def item(self, params):
        #--------------Description
        # IN     : 
        # OUT    : Status / Data
        # Action : Items

        #--------------Variable
        output = {}
        output["status"] = True

        #--------------Action
        id = params["item"]
        output['data'] = f"item {id} "

        #----------Return
        return output

   #-------------------------- [Add]
    def add(self, params):
        #--------------Description
        # IN     : 
        # OUT    : Status / Data
        # Action : Add item

        #--------------Variable
        output = {}
        output["status"] = True

        #--------------Action
        item = params["item"]
        id = item.id
        name = item.name
        output['data'] = f"item {id} | {name}  added"

        #----------Return
        return output
    
   #-------------------------- [Edit]
    def edit(self, params):
        #--------------Description
        # IN     : 
        # OUT    : Status / Data
        # Action : Edit item

        #--------------Variable
        output = {}
        output["status"] = True

        #--------------Action
        item = params["item"]
        id = item.id
        name = item.name
        output['data'] = f"item {id} | {name}  edited"

        #----------Return
        return output
    
    #-------------------------- [Delete]
    def delete(self, params):
        #--------------Description
        # IN     : 
        # OUT    : Status / Data
        # Action : Delete item

        #--------------Variable
        output = {}
        output["status"] = True

        #--------------Action
        item = params["item"]
        id = item.id
        name = item.name
        output['data'] = f"item {id} | {name}  deleted"

        #----------Return
        return output
