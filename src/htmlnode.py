
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
       self.tag = tag
       self.value = value
       self.children = children
       self.props = props


    def to_html(self): 
        raise NotImplementedError()

    
    def props_to_html(self) -> str:
        props_str = ""
        
        if self.props:
            for t in self.props.items():
                props_str += f"{t[0]}=\"{t[1]}\" "

        return props_str


    def __repr__(self) -> str:
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All Leaf nodes must have a value")

        if self.tag == None:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"
