# JSONPlaceholder 
**json fake REST Flask API for testing and rapid prototyping**

JSONPlaceholder is a simple configurable python flask REST API for testing and rapid prototyping.

it's an alternative to the javascript JSONPlaceholder but more inclined for personal testing or development for developers.

### Features
- No API key, or JSON Token
- Full REST Compliant
- GET, POST, METHOD
- Easily Configurable
- Cors Header support



### Resources
* /posts


```python
python app.py

 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://localhost:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 108-855-129

```


### Usage
`A simple example making use of localhost to get a list of post `

```javascript
fetch('http://localhost:8080/posts')
	.then(response => response.json())
	.then(data => console.log(data))

```


### Filter
Specific posts can also be searetrieved using `/posts/2` where 2 refers to the id number `<posts/<id>` 

### CORS bypass
> Edit the `app.py` file and add the url of the server to the whitelist variable
i.e.
```python
whitelist  =  ['http://localhost', 'http://localhost:5577', 'http://127.0.0.1:5577',, 'http://127.0.0.1', http://localhost:5578']
```

### Usage
`jsonPlaceHolder` can be used  within a javaScript to retrieve data from server

```javascript

fetch("http://localhost:8080/posts", {
	method: 'PUT',
	headers: {
		'Content-Type': 'application/json'
	},
	body: JSON.stringify({title: 'John Doe', body: 'A name with no significance'})
})
	.then(response => response.json())
	.then(data => console.log(data));
```
