import tkinter as tk

root = tk.Tk()
root.title('Trie Autocomplete Visualization')

app_width = 1000
app_height = 500

root.geometry(f'{app_width}x{app_height}+{100}+{100}')

root.configure(background='white')

def update(data):
    my_list.delete(0, tk.END)

    for item in data:
        my_list.insert(tk.END, item)

def fillout(e):
    my_entry.delete(0, tk.END)
    my_entry.insert(0, my_list.get(my_list.curselection()))

def check(e):
    typed = my_entry.get()

    if typed == '':
        data = toppings
    else:
        data = []
        for item in toppings:
            if typed.lower() in item.lower():
                data.append(item)
    update(data)  


def trieList(e):
    trie_entry.delete(0, tk.END)
    trie_entry.insert(0, my_list.get(trie_list.curselection()))

def updateTrie(data):
    trie_list.delete(0, tk.END)

    for item in data:
        trie_list.insert(tk.END, item)





# Create a label
label = tk.Label(root, text="Start Typing...", font=("Helvetica", 26), fg="black")
label.configure(background='white')
label.pack(pady=20)

my_entry = tk.Entry(root, font=("Helvetica", 18), width=22)
my_entry.configure(background='white')
my_entry.pack()

my_list = tk.Listbox(root, width=50)
my_list.configure(background='white')
my_list.pack(pady=40)

trie_entry = tk.Entry(root, font=("Helvetica", 18), width=22)
trie_entry.configure(background='white')
trie_entry.pack()

trie_list = tk.Listbox(root, width=50)
trie_list.configure(background='white')
trie_list.pack(pady=40)


toppings = ["Pepperoni", "Peppers", "Mushrooms", "Cheese", "Onions", "Ham"]
update(toppings)


# Double<> for listbox
my_list.bind("<<ListboxSelect>>", fillout)

my_entry.bind("<KeyRelease>", check)

trie_list.bind("<<ListboxSection>>", trieList)


root.mainloop()

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
    
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
myTrie = Trie()
myTrie.insert("happy")
myTrie.insert("hello")
myTrie.insert("hi")
myTrie.insert("hand")
myTrie.insert("hank")



print(myTrie.startsWith("h"))
updateTrie(myTrie.startsWith("h"))
