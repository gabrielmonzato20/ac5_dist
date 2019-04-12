from flask import Flask,jsonify,request

app = Flask(__name__)
alunos = []
professorres = []
@app.route('/alunos')
def retorna_alunos():
    return jsonify(alunos)
@app.route('/alunos', methods=['POST'])
def add_aluno():
    new = request.json
    if 'nome' not in new.keys():
        return jsonify({'erro':'aluno sem nome'}),400
    for aluno in alunos:
        if aluno['id'] == new['id']:
            return jsonify({'erro':'id ja utilizada'}),400
   
    alunos.append(request.json)
    return jsonify(alunos),200
 
@app.route('/alunos/<int:id>')
def retorna_aluno_id(id):
    for aluno in alunos:
        if aluno['id'] == id:
            return  jsonify(aluno) 
    return jsonify({'erro':'aluno nao encontrado',}),400
@app.route('/reseta',methods=['POST'])
def reseta_alunos():
    alunos.clear()
    professorres.clear()
    return jsonify({'ok':'resetado com sucesso'}),200
@app.route('/alunos/<int:id>',methods=['DELETE'])
def delete_aluno(id):
    for index,aluno in enumerate(alunos):
        if aluno['id'] == id:
           del alunos[index]
    return jsonify({'erro':'aluno nao encontrado',}),400
@app.route("/alunos/<int:id>",methods=['PUT'])
def edita(id):
    dados = request.json
    if  'nome' not in dados.keys():
        return jsonify({'erro':'aluno sem nome'}),400
    for aluno in alunos:
        if aluno['id'] == id:
            aluno['nome'] = dados['nome']
            return jsonify(alunos)
  
    return jsonify({'erro':'aluno nao encontrado',}),400
@app.route("/professores",methods=['GET'])
def professor_show():
    return jsonify(professorres)
@app.route("/professores",methods=['POST'])
def add_prof():
    prof=request.json
    professorres.append(prof)             
@app.route('/professores/<int:id>')
def retorna_professor(id):
    for professor in professorres:
        if professor['id'] == id:
            return jsonify(professor)
    return jsonify({'erro':'professor nao encontrado'}),400
if __name__ == '__main__':
    app.run(port=5002,debug=True,host='localhost')