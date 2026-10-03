import sys
sys.path.append('./')

from connection import db_session
from model.sql_model import Todo
import decoders.todo as decode


def create_todo(todo: str) -> dict:
    try:
        req = Todo(todo)
        db_session.add(req)
        db_session.commit()
        return {
             'status': 'ok',
             'message': 'Todo created successfully'
             }
    except Exception as e:
        return {
             'status': 'error',
             'message': str(e)
             }


def get_all_todos() -> list:
    try:
        res = db_session.query(Todo).all()
        docs= decode.decode_todos(res)
        return {
            'status': 'ok',
            'data': docs
        }
    except Exception as e:
        return {
            'status': 'error'
        }

        
def get_todo(_id: int) -> dict:
    try:
        criteria = {'_id': _id}
        res = db_session.query(Todo).filter_by(**criteria).one_or_none()
        if res is not None:
            record = decode.decode_todo(res)
            return {
                'status': 'ok',
                'data': record
            }
        else:
            return {
                'status': 'error',
                'message': f'record with id {_id} does not exists'
            }
    except Exception as e:
        return {
            'status': 'error'
        }

        
def update_todo(_id: int, _title: str) -> dict:
    try:
        criteria = {'_id': _id}
        res = db_session.query(Todo).filter_by(**criteria).one_or_none()
        if res is not None:
            res.todo = _title
            db_session.add(res)
            db_session.commit()
            return {
                'status': 'ok',
                'message': 'record updated successfully'
            }
        else:
            return {
                'status': 'error',
                'message': f'record with id {_id} does not exists'
            }
    except Exception as e:
        return {
            'status': 'error'
        }

def delete_todo(_id: int) -> dict:
    try:
        criteria = {'_id': _id}
        res = db_session.query(Todo).filter_by(**criteria).one_or_none()
        if res is not None:
            db_session.delete(res)
            db_session.commit()
            return {
                'status': 'ok',
                'message': 'record deleted successfully'
            }
        else:
            return {
                'status': 'error',
                'message': f'record with id {_id} does not exists'
            }
    except Exception as e:
        return {
            'status': 'error'
        }

# res = create_todo('Buy groceries')
# print(res)

# res = get_all_todos()
# print(res)

# res = get_todo(12)
# print(res)

# res = update_todo(1, 'website updated')
# print(res)


# res = delete_todo(1)
# print(res)