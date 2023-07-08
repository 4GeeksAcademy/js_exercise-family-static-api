import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the Jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }
    return jsonify(response_body), 200

@app.route('/members', methods=['POST'])
def add_family_member():
    member_data = request.json
    age = member_data.get("age")
    first_name = member_data.get("first_name")
    lucky_numbers = member_data.get("lucky_numbers")
    
    if age is None:
        return jsonify({"error": "Missing age"}), 400
    if first_name is None:
        return jsonify({"error": "Missing first name"}), 400
    if lucky_numbers is None:
        return jsonify({"error": "Missing lucky numbers"}), 400
    
    jackson_family.add_member(
        {
            "id": jackson_family.generate_id(),
            "first_name": first_name,
            "last_name": jackson_family.last_name,
            "age": age,
            "lucky_numbers": lucky_numbers
        }
    )
    
    return jsonify({"message": "Family member has been added"}), 200

@app.route("/delete/<int:id>", methods=['DELETE'])
def delete_family_member(id):
    response = jackson_family.delete_member(id)
    if response is True:
        response_body = {"Family Member Deleted": True}
        return jsonify(response_body), 200
    else:
        response_body = {"Wrong ID": False}
        return jsonify(response_body), 200
    
@app.route("/member/<int:id>", methods=['GET'])
def get_individual_family_member(id):
    member = jackson_family.get_member(id)
    if member is None:
        return jsonify({"error": "Family member not found"}), 404
    else:
        return jsonify(member), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
