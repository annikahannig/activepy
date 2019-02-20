
"""
A simple example for a command and multiple handlers
"""

import random

import active

class CreateUserRequest(active.Action): pass
class CreateUserResponse(active.Action): pass

class CreateUserSuccess(active.Action): pass
class CreateUserError(active.Action): pass


@active.command
def create_user(dispatch, request):
    """Create a user"""
    if request.username == "admin":
        print("Not creating user because reason.")
        dispatch(CreateUserError(message="Can not be admin!"))

        return CreateUserResponse(
            status="ERROR")

    print(f"Creating user: {request.username}")
    # ... rest of the owl
    user_id = random.randint(230, 420)
    user = {
        "username": request.username,
        "id": user_id,
    }

    dispatch(CreateUserSuccess(user=user))

    return CreateUserResponse(
        status="OK",
        user=user)


@active.handler(
    CreateUserSuccess,
    CreateUserError)
def update_user_state(action):
    """Something happened. Update some state."""
    print("Updating user state with action:", action)


@active.handler(CreateUserSuccess)
def log_success(action):
    """User was successfully created"""
    print("Created user:", action.user)
