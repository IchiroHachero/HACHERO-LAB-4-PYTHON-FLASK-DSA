# Ichiro Hachero
# BSCPE 2-1
from flask import Flask, render_template, request

app = Flask(__name__)
#link list operation
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class CustomLinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, value):
        new_node = LinkedListNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if self.head:
            self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def to_list(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.value)
            current = current.next
        return nodes


linked_list_demo = CustomLinkedList()

#link list rute
@app.route('/works/linked-list', methods=['GET', 'POST'])
def linked_list_page():
    message = ""
    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value', '').strip()

        if action == 'add_bg':
            if value:
                linked_list_demo.add_at_beginning(value)
                message = f"Added '{value}' at beginning."
        elif action == 'add_end':
            if value:
                linked_list_demo.add_at_end(value)
                message = f"Added '{value}' at end."
        elif action == 'del_bg':
            linked_list_demo.delete_at_beginning()
            message = "Deleted node from beginning."
        elif action == 'del_end':
            linked_list_demo.delete_at_end()
            message = "Deleted node from end."

    return render_template(
        'linked_list.html',
        nodes=linked_list_demo.to_list(),
        message=message
    )
#Linked list
class Node:
    def __init__(self, location, status):
        self.location = location
        self.status = status
        self.next = None


class SuspensionHistory:
    def __init__(self, max_size=5):
        self.head = None
        self.size = 0
        self.max_size = max_size

    def add_search(self, location, status):
        new_node = Node(location, status)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

        if self.size > self.max_size:
            current = self.head
            for _ in range(self.max_size - 1):
                if current.next:
                    current = current.next
            if current:
                current.next = None
            self.size = self.max_size

    def to_list(self):
        results = []
        current = self.head
        while current:
            results.append({
                'location': current.location,
                'status': current.status
            })
            current = current.next
        return results


history_ll = SuspensionHistory(max_size=5)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


#Works
@app.route('/works')
def works():
    return render_template('works.html')


#To Uppercase
@app.route('/works/uppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)


@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    if request.method == 'POST':
        radius = request.form.get('radius', '')
        if radius:
            result = float(radius) * 3.14159 * float(radius)
    return render_template('circle.html', result=result)


@app.route('/works/area/triangle', methods=['GET', 'POST'])
def atriangle():
    result = None
    if request.method == 'POST':
        base = request.form.get('base', '')
        height = request.form.get('height', '')
        if base and height:
            result = 0.5 * float(base) * float(height)
    return render_template('triangle.html', result=result)


@app.route('/works/suspension-checker', methods=['GET', 'POST'])
def check_suspension():
    location = ""
    status = "MAY PASOK PO"

    if request.method == 'POST':
        location = request.form.get('location', '').strip()
        if location:
            history_ll.add_search(location, status)

    return render_template(
        'check.html',
        location=location,
        status=status,
        history=history_ll.to_list()
    )


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)