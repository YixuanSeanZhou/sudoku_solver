# React

### JSX

* Use HTML in javascript
* Create a UI elememt in Javascript

```react
const element = <h1>Hello, world!</h1>;

// Needed to render the whole page
ReactDOM.render(
  element,
  // If all the page is created by React, this is the only element needed in html
  document.getElementById('root')
);
```

To use varibale in JSX uses curly brace 

```react
const name = 'Josh Perez';
const element = <h1>Hello, {name}</h1>
```

JSX is also an expression in JavasScript you can use it like:  `return <h1>Hello, Stranger.</h1>;`

To specify attributes in JSX, can use either string or curly brace but not both 

```react
// Either
const element = <div tabIndex="0"></div>;
// Or
const element = <img src={user.avatarUrl}></img>;
```

	##### Object with JSX

```react
const element = (
  <h1 className="greeting">
    Hello, world!
  </h1>
);
```

<u>**React Objects Are Immutable **</u>



### Render

To rander the object / jsx created in React to DOM(HTML), need to use `ReactDOM.render()` method and in side the param should be the element created to be rendered, the element in DOM to append child to.

Example:

```react
const element = <h1>Hello, world</h1>;
ReactDOM.render(element, document.getElementById('root'));
```

Even though as stated above, objects / UI are immutable, but you can re-render it to modify the attributes.

###### React Only update what is necessary when re-render

React DOM compares the element and its children to the previous one, and only applies the DOM updates necessary to bring the DOM to the desired state.



##### Create a tick clock

The followingh code create a tick clock

```react
function tick() {
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(element, document.getElementById('root'));
}

/* This is not a React Component, but rather from web api that will call the tick method with a intervral of 1000 */
setInterval(tick, 1000);
```



### Components and Props 

To define a component, we can define a `class` or`function` just like declearing an object in JavaScript

```react
// Traditional JavaScript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

// ES6
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}

// Below to put multiple child elements in a parent element and render together
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```

*Note: Because of the fact that React modify the whole component, so we want to factorize the components as much as possible. Such as, don't put a lot of tags in one component, we put it into different child componenents instead.*



##### props

The JSX attribute is passed in as an object to the component if React sees an user defiened JSX object, the JSX attribute is `props`.

```react
const element = <Welcome name="Sara" />;
```

In this case, the props has a value that is name, so we can access in the definiation of `Welcome` as `props.name`



### State and LifyCycle

From here, the major usage of component will be using `class` since it provides the accsses to state.

Continue from the above tick clock example, we can define a clock like this

```React
class Clock extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.props.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
```

However, we want React to update the clock with every sec, but it does not do that right now. 

We still can use the setInterval method but right now we don't have the access to the Date object.



Therefore we need a state attribute so that React konws when to update what.

To initilize any attributes of a class, we need `constructor` method of the class.

```react
// The props is passed in as a parameter of the constructor.
constructor(props) {
  // All the constructor has of a class has to call super at the very begining.
  super(props);
  this.state = {date: new Date()};
}
```



##### Lifecycle methods

Now with a constructor, we want to add a life cycle method so that we can effectively and effeciently use the object that we defined, that is saying the method can be stoped when the object is no longer needed.

The two lifecycle methods are `componentDidMount()` and `componentWillUnmount()`. 



###### Execution time

`constructor()` run before the component mount

`componentDidMount()` run after the component is rendered

`componentWillUnmount()` run before unmount.



In our clock case, we want to call the tick method that update the time of our clock when the clock ojbect is rendered and stop the tick method when the clock component is going to unmount

```react
componentDidMount() {
  this.timerID = setInterval(
  () => this.tick(),
  1000
  );
}
// clearInterval take in the Id returned by setInterval (like memset and free in C)
componentWillUnmount() {
  clearInterval(this.timerID);
}
```



##### Update State

Now we need to write the tick method for our clock object. 

```react
tick() {
  // Here we modify the state so that react knows to rerender
  // Note: we are passing in a new object to the setState parameter. 
  // So instead of modifying the state, we are creating a new state
	this.setState({
    date: new Date()
	});
}
```



###### State Update Maybe Asynchronous 

If we want to use props as a parameter when setState, the update maybe asynchronous, that is this.props and this.state is not reliable when calculating the next stage.

```react
// Wrong
this.setState({
  counter: this.state.counter + this.props.increment,
});

// Correct 
// becaues in this case we are using the pre-stored value at one point before updates
this.setState((state, props) => ({
  counter: state.counter + props.increment
}));
```

###### Can update the state independently for different attributes of the state



##### Share Data Accross Components 

To collect data from multiple children, or to have two child components communicate with each other, you need to declare the shared state in their parent component instead. 

The parent component can <u>pass the state back down</u> to the children by using props; this *keeps the child components in sync* with each other and with the parent component.



##### Immutability 

All the React objects should be updated with immutable approach, because they are easier to compare and easier to determine when should be compunent be updated. [`shouldComponentUpdate()`](https://reactjs.org/docs/optimizing-performance.html#examples) 

Therefore in react, we prefer the function that does not modify the original thing, that is saying using `concat()`  instead of `push()` and so on.



#### Handling Events

**Naming Convension:** camelCase

**Event Handler:** Pass in a function instead of a string that is a name of a function.

To prevent the default behavior of an element, say when a link is clicked, the default is to jump to that link, to prevent that, in the eventHandler function, we need to call preventDefault() on the event.

**Binding:** React's function is not auto-bound. As a result, in a classs's constructor, we need to explicitly call `bind()` method on the function that we want to specify `this` key word.

*Generally, if we refer the function without (), that is onClick = {this.handleClick}, we need binding*



#### Conditional Rendering

&& Operator can be handy because True && Exp = Exp, False && Exp = False

```react
{unreadMessages.length > 0 &&
  <h2>
    You have {unreadMessages.length} unread messages.
  </h2>
}
```





#### Lists & Keys

We can use the JavaScripts' `map()`  function to convert an array to a JSX list element.

```react
const numbers = [1, 2, 3, 4, 5];
const listItems = numbers.map((number) =>
  <li>{number}</li>
);
                              
ReactDOM.render(
  <ul>{listItems}</ul>,
  document.getElementById('root')
);
```



We can also refactor this into a component of React

```react
// This component is reuseable
function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>
    <li>{number}</li>
  );
  return (
    <ul>{listItems}</ul>
  );
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
  <NumberList numbers={numbers} />,
  document.getElementById('root')
);
```



However, when creating lists of elements, we need to assign `key` to each list element `<li>` such that react can make comprision of what to compare and what to re-render. So the above code does not work. We need to add key attribute to the `<li>`

```react
function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>
    <li key={number.toString()}>
      {number}
    </li>
  );
  return (
    <ul>{listItems}</ul>
  );
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
  <NumberList numbers={numbers} />,
  document.getElementById('root')
);
```



##### Keys

> A “key” is a special string attribute you need to include when creating lists of elements.

Usually the key is the IDs from data, but sometime can use indexes, which is not recommended. 

```react
const todoItems = todos.map((todo) =>
  <li key={todo.id}>
    {todo.text}
  </li>
);

const todoItems = todos.map((todo, index) =>
  // Only do this if items have no stable IDs
  <li key={index}>
    {todo.text}
  </li>
);    
```



#### Forms

The forms in React is impelemented via *Controlled Components*

An example of a controlled component:

```react
class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Name:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}
```

In this way, the react component is the sigle ssource of truth that konws the state and render the form.

In this way, the displayed value of the form will also be alined with the state.value attribute. Therefore we can enforce, say name has to be all upper case, by changing #11 to `this.setState({value: event.target.value.toUpperCase()});`



###### Differences between html - textarea tag

The `textarea` tag defines its text by its children in html : 

```html
<textarea>
  Hello there, this is some text in a text area
</textarea>
```

But in react, it is defined by its value attribute

```react
lass EssayForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: 'Please write an essay about your favorite DOM element.'
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('An essay was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Essay:
          <textarea value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}
```

Note: The state is init by the constructor.











