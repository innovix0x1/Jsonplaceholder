import json

from flask import Flask, abort, make_response, request
from flask.wrappers import Response

app = Flask(__name__)

@app.route('/posts', methods=['GET'])

def get_all():
    
    fd = open('posts.json', 'r')  # type: ignore
    data = json.loads(fd.read())
    
    post = data
    if len(post) == 0:
        abort(404)
        
    return Response(json.dumps(post, indent=4), mimetype='application/json')

    
@app.route('/posts/<int:id>', methods=["GET"]) 

def query_records(id):
    
    if( int(id) == 0 ):
        abort(400)
    
    id = id -1
    # records = open('r')
    fd = open('posts.json', 'r')  # type: ignore
    data = json.loads(fd.read())
    

    # for d in data.values():
    #     task.append(d)
    
    post = [ task for task in data.values() ][0][id]
    
    
    if (len(post) == 0):
        abort(404)
    
    
    return Response(json.dumps(post, indent=4), mimetype='application/json')
    
@app.route('/posts', methods=['POST'])

def post_record():
    # content_type = request.args.get('Content-Type')
    # if (content_type == 'application/json'):
        # post = json.loads(request.data)
    
    
    
    if not (request.is_json) or not ('title' in request.data.decode()):
        abort(400)
        
    with open('posts.json', 'r') as  fp:
        data = fp.read()
        data = json.loads(data)
        
        content = request.json

        task = {
            'id': data['posts'][-1]['id'] + 1,
            'title': content['title'], # can also use content.get(''title)
            'body': content['body']
        }
        fp.close()
    
   
    
    fp = open('posts.json', 'w+')
    data['posts'].append(task)  
    

    json.dump(data, fp)
    fp.close()
    
    
    return Response(json.dumps(task, indent=4), mimetype='application/json')
    
            
            
            
        # record = open()
        #return Response(json.dumps(post, indent=4), mimetype='application/json')
    # else:
        # return 'Content-Type not Supported!'
        
    
       
    

@app.route('/posts/<int:id>', methods=['PUT'])

def put_record(id):
    content = request.get_json()
   
    if (id == ''):
        make_response(
            {
            'error': 'id not set'
            }, 404
        
        )
        
    if( int(id) == 0 ):
        abort(404)
     
    if not request.json:
        abort(400)
    
    try:
        if not (content['title']) or not(content['body']):
            abort(400)
    except KeyError as err:
        print(f"Keys - 'body' or 'title' not in request body, Error - {err}")
        abort(500)
         
   
    if not (type(content['title']) != 'unicode' and type(content['body']) != 'unicode'):
        abort(500)

        
    fd = open('posts.json', 'r')  # type: ignore
    data = json.loads(fd.read())
    fd.close()
    
    if len(data.get('posts')) == 0:
        abort(404)
        
    
    data.get('posts')[id-1]['title'] = request.json.get('title')
    data.get('posts')[id-1]['body'] = request.json.get('body') 
    

    fd = open('posts.json', 'w')
    json.dump(data, fd)
    fd.close()
    
    task = dict()
    task['id'] =  id
    task['title'] = request.json.get('title')
    task['body'] = request.json.get('body')
    
    return Response(json.dumps(task, indent=4), mimetype='application/json')


@app.route('/posts/<int:id>', methods=['DELETE'])

def remove_post(id):
    if (id == ''):
        make_response(
            {
            'error': 'id not set'
            }, 404
        
        )
        
    if( int(id) == 0 ):
        abort(404)
        
    
    id = id -1
    # records = open('r')
    fd = open('posts.json', 'r')  # type: ignore
    data = json.loads(fd.read())
    
    
    post = [ task for task in data.values() ][0][id]
    
    post['id']
    
    if len(data.get('posts')) == 0:
        abort(404)

    return Response(json.dumps(data, indent=4), mimetype='application/json')

@app.errorhandler(404)

def notFound(error):
    return make_response(
        {
            'error': 'Resource Not found'
    }, 404)
    
whitelist = ['http://localhost', 'http://localhost:5577', 'http://127.0.0.1:5577', 'http://127.0.0.1', 'http://127.0.0.1:5578', 'http://localhost:5578']
    
@app.after_request

def add_cors_headers(response):
    
    if request.headers.get('Origin') in whitelist:
        response.headers.add('Access-Control-Allow-Origin', request.headers['Origin'])
        response.headers.add('Access-Control-Allow-Headers', "Content-Type")
        response.headers.add('Access-Control-Allow-Header', "Cache-Control")
        # response.headers.add('Connection', 'open')
        response.headers.add("Access-Control-Allow", ' X-Requested-With')
        response.headers.add("Access-Control-Allow-Headers",  'Authorization')
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, PUT, UPDATE")
    
        return response
    else: 
        return response
    
      
@app.errorhandler(405)

def methodNotAllowed(error):
    return make_response(
        {
            'error': 'Method not Allowed'   
        }
    )


@app.errorhandler(500)

def server_error(error):
    return make_response(
        {
        'error': 'Request Type not supported'
        }, 500
    )
    
@app.errorhandler(400)

def badRequest(error):
    return make_response(
        {
            'error': 'Content-Type not Supported!'
    }, 400)
          
            
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)


# /posts title , body
