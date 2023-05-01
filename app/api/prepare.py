from flask import jsonify, request, g, url_for
from flask import current_app as app
from .. import db, socketIo
from . import api
import os
import threading
from ..preparator.Preparator import check_condition, prepare_folder, progress

@api.route('/prepare/check_folder_condition/home/<path:req_path>', methods=['GET', 'POST'])
@api.route('/prepare/check_folder_condition/<path:req_path>', methods=['GET', 'POST'])
def prepare_check_folder_conditions(req_path):
    print(req_path)
    abs_path = os.path.join(app.config['SRC_FOLDER'], req_path)
    print(abs_path)
    conditions = check_condition(abs_path)
    return conditions, 200

@api.route('/prepare/prepare_folder/home/<path:req_path>', methods=['POST'])
@api.route('/prepare/prepare_folder/<path:req_path>', methods=['POST'])
def prepare_prepare_folder(req_path):
    abs_path = os.path.join(app.config['SRC_FOLDER'], req_path)
    msg = prepare_folder(app.config['SRC_FOLDER'], app, req_path)
    print(msg)
    return jsonify({"Status":"ok"}), 200

@api.route('/prepare/progress/home/<path:req_path>', methods=['GET'])
@api.route('/prepare/progress/<path:req_path>', methods=['GET'])
def prepare_folder_progress(req_path):
    converted_file_count, total_files = progress(req_path, app)
    return jsonify({'current': converted_file_count, 'total': total_files})

