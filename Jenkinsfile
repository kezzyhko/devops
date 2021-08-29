pipeline {
  environment {
    imagename = "kezzyhko/devops"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Build') {
      steps {
        script {
          dockerImage = docker.build imagename
        }
      }
    }
    stage('Test') {
      steps {
        script {
          dockerImage.inside {
            sh 'python3 manage.py test'
          }
        }
      }
    }
    stage('Push') {
      steps {
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push("$BUILD_NUMBER")
            dockerImage.push('latest')
          }
        }
      }
    }
    stage('Clean up') {
      steps {
        sh "docker rmi $imagename:$BUILD_NUMBER"
        sh "docker rmi $imagename:latest"
      }
    }
  }
}