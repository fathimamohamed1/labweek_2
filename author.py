

#running different tests to see if the Author c;ass and its published methods are running smoothly
def main():
    colleen= Author('Collen Hoover')
    colleen.publish('verity')
    print(colleen.name)
    print(colleen.books)
    hyaat= Author('Hyaat West')
    hyaat.publish('best year ever')
    print(hyaat.name)
    print(hyaat.books)
    hyaat.publish ('best year ever')
    dale= Author ('Dale Carnage')
    dale.publish('dale is dily dallying around')
    print(dale.name)
    print(dale.books)
    fathima=Author('Fathima')
    print(fathima)


class Author:
    def __init__(self,name):  
     self.name = name
     self.books=[]

     #self.books = becomes a set()

    def __str__(self):
       # titles= ','.join(self.books) 
       #return f'{self.name}, Books:{titles}'
        if self.books:
            book_list= ','.join(self.books)  #if author has book published it will be added to the published book list 
    
            
        else:
            book_list='No  books'
            return f'Name :{self.name}, Published books:{book_list}' # if author does nothave a book published the no book message will be seen 

    def publish(self,book):

        if book in self.books:
            print('Unfortunately this books been already been added.')  #error message when duplicate book name is mentioned 
        else:
            self.books.append(book) #if not in list it will be added to the list 

        

main ()
        










