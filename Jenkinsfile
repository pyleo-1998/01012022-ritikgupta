pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/pyleo-1998/29122021-ritikgupta.git']]])
            }
        }
        stage("Build")
        {
            steps{
                git branch: 'main', url: 'https://github.com/pyleo-1998/29122021-ritikgupta.git'
                bat 'pip3 install --no-cache-dir -r requirements.txt'
                bat 'python json_reader_converter.py'
            }
        }
        stage("Test")
            {
            steps{
                bat 'python data_analysis.py'
            }
        }
    }
    post{
        success{
            echo "successfully Setup,build and test the application"
        }
    }
}