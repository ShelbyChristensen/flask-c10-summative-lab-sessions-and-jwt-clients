from flask import Blueprint, request, session, jsonify
from app import db
from models import Note

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('', methods=['GET'])
def index_notes():
    user_id = session.get('user_id')
    if not user_id:
        return {'error': 'Unauthorized'}, 401

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    notes = Note.query.filter_by(user_id=user_id).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify([{'id': n.id, 'title': n.title, 'content': n.content} for n in notes.items])

@notes_bp.route('', methods=['POST'])
def create_note():
    user_id = session.get('user_id')
    if not user_id:
        return {'error': 'Unauthorized'}, 401

    data = request.get_json()
    note = Note(title=data['title'], content=data['content'], user_id=user_id)
    db.session.add(note)
    db.session.commit()
    return {'id': note.id, 'title': note.title, 'content': note.content}, 201

@notes_bp.route('/<int:id>', methods=['PATCH'])
def update_note(id):
    user_id = session.get('user_id')
    if not user_id:
        return {'error': 'Unauthorized'}, 401

    note = Note.query.get_or_404(id)
    if note.user_id != user_id:
        return {'error': 'Forbidden'}, 403

    data = request.get_json()
    note.title = data.get('title', note.title)
    note.content = data.get('content', note.content)
    db.session.commit()
    return {'id': note.id, 'title': note.title, 'content': note.content}, 200

@notes_bp.route('/<int:id>', methods=['DELETE'])
def delete_note(id):
    user_id = session.get('user_id')
    if not user_id:
        return {'error': 'Unauthorized'}, 401

    note = Note.query.get_or_404(id)
    if note.user_id != user_id:
        return {'error': 'Forbidden'}, 403

    db.session.delete(note)
    db.session.commit()
    return {}, 204
