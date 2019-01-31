pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.4-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile adder.py adder_test.py' 
            }
        }
    }
}
