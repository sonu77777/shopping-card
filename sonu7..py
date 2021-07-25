class shoppingCart:
    customer_name=None
    current_date=None
    cart_items=[]

      def  add_item(self,ItemToPurchase):  
         self.cart_items.append(ItemToPurchase)

      def get_cost_of_cart(self):
          tot=0
          for i in range(len(self.cart_items)):
              t=self.cart_items[i].split(":")
              cost=int(t[-2])*int(t[-1])
              tot+=cost
              return tot
        def print_total(self):
            if len(self.cart_items)==0:
                print("SHOOPING CART IS EMPTY")
             else:
                 print("OUTPUT SHOPPING CART")
                 print(self.customer_name+"'s shopping cart-" self.current_date)
                 print("NUmber of items:",end="")
                 n=0
                 for i in range(len(self.cart_items)):
                     t=self.cart_items[i].split(":")
                     print(n)
                     print()
                  for i in range(len(self.cart_items)):
                      t=self.cart_items[t].split(":")
                      print(t[0]+""+t[-1]+"@ &"+t[-2]+"=",end="&")
                      cost=int(t[-2])*int(t[-1])
                      print(cost)
                      print()
                      print("Total:&",end="")
                      print(self.get_cost_of_cart())
          def print_description(self):
              print("OUTPUT ITEMS DESCRIPTION")
              print(self.customer_name + "'s shopping cart -" +self.cureent_date)
              print()
              print("Item Description")

              for i in range(len(self.cart_item)):
                  t=self.cart_items[i].split(":"):
                   print(t[0] + ": "+t[1]
          def get_num_items_in_cart(self):
              c=0
              for i in range(len(self.cart_items)):
                  t=self.cart_items[i].split(":")
                  c+=int(t[-1])
                  return c

          def remove_item(self,name):
              for i in range(len(self.cart_items)):
                  t=self.cart_items[i].split(":")
                  if t[0]==name:
                      self.cart_items.remove(self.cart_item[i])
                      break
                else:
                    print("Item not found in cart. nothing removed.")
            def modify_item(self,ItemTOPurchase):
                for i in range(len(self.cart_item)):
                    t=self.cart_items[i].split(":")
                    n=ItemToPurchase[0]
                    q=ItemToPurchase[1]
                    ift[0]==n:
                        d=t[1]
                        p=t[2]
                        temp=n+":"+d":"+str(p)+":"+str(q)
                        self.cart_items_removed(self.cart_item[i])
                        self.add_item(temp)
                        break
                    else:
                        print("Item not found in cart.Nothing removed.")
                        
                
                  

            
          
    
