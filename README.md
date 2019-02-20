
# ActivePY

This is some mashup between some actor pattern, reactive programming
and python decorators.


## The User Facing API

Consider having an architecture of a larger application like

    app
     |-- users/models.py
     |-- users/services/user_svc.py

Where the `user_svc` encapsulates interacting with the
model classes for later refactoring from a monolith into
microservices. 

We now have this kind of api:

```python
result = user_svc.create_user(
    CreateUserRequest(username="user", name="Foo Bar"))
```

Where everything the service requires is encapsulated in a
request object. (We might want to transmogrify the request object
into some grpc request later.)


### The Service Layer

The service is split into `handlers` and `commands`.
What you saw above is the execution of a `create_user` command.

Commands are unary functions, accepting a request and returning
a response.

Events might be dispatched during the execution of the command.

So let's define some actions first:

```python
class CreateUserRequest(active.Action): pass
class CreateUserResponse(active.Action): pass

class CreateUserSuccess(active.Action): pass
class CreateUserError(active.Action): pass
```

We can now use these to implement some create user function:

```python
@active.command
def create_user(dispatch, request):
    """Create a user"""
    if request.username == "admin":
        dispatch(CreateUserError(message="Can not be admin!"))
        return CreateUserResponse(status="ERROR")

    user_id = random.randint(230, 420)
    user = {"username": request.username, "id": user_id}

    dispatch(CreateUserSuccess(user=user))

    return CreateUserResponse(
        status="OK",
        user=user)
```

Great! Let's attach some handlers to this!

Handlers are only called if the action matches 
one of the required types.

```python
@active.handler(
    CreateUserSuccess,
    CreateUserError)
def update_user_state(action):
    """Something happened. Update some state."""
    print("Updating user state with action:", action)
```

Maybe add some logging:

```
@active.handler(CreateUserSuccess)
def log_success(action):
    """User was successfully created"""
    print("Created user:", action.user)

```

And that's basically it.



