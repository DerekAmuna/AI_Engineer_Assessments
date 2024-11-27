provider "aws" {
  region = "us-east-1"
}



resource "aws_elastic_beanstalk_application" "flask_app" {
  name        = "ChurnPrediction"
  description = "Flask App for Churn Prediction"
}

resource "aws_elastic_beanstalk_environment" "flask_env" {
  name                = "ChurnPrediction-env"
  application         = aws_elastic_beanstalk_application.flask_app.name
  solution_stack_name = "64bit Amazon Linux 2023 v4.3.1 running Python 3.11"




  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "FLASK_ENV"
    value     = "production"
  }
}

output "beanstalk_url" {
  value = aws_elastic_beanstalk_environment.flask_env.endpoint_url
}
