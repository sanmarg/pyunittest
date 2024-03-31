pipeline {
    agent any

    stages {
        stage('https://atg.world') {
            steps {
                sh 'rm -rf pyunittest'
                sh 'git clone https://github.com/sanmarg/pyunittest.git'
                sh 'python3 pyunittest/main.py'
            }
        }
        stage('hello.unaux.com'){
            steps {
                sh 'python3 pyunittest/main.py https://hello.unaux.com'
            }
        }
        stage('stage of invalid url'){
            steps {
                sh 'python3 pyunittest/main.py https://atggg.woorld'
            }
        }
    }
}
