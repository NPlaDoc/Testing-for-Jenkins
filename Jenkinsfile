pipeline {
  agent any
  stages {
    stage('Clone'){
        steps{
            git branch: 'main', url: 'https://github.com/NPlaDoc/Testing-for-Jenkins.git'
	}
    }	
    stage('Run npm dev') {
      steps {
        sh 'npm run dev'  // This will execute the npm run dev command
      }
    }		  
    // stage('Run Python Script') {
    //   steps {
    //     script {
    //       // Define Python interpreter path (if not in PATH)
    //       def pythonPath = '/usr/bin/python3' // Adjust path as needed
          
    //       // Execute the script
    //       sh "${pythonPath} my_script.py"
    //     }
    //   }
    // }
  }
}
