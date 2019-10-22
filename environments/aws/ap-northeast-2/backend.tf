terraform {
  required_version = ">= 0.11.0"

  backend "s3" {
    region = "ap-northeast-1"
    bucket = "cirgar-crawler-tfstate"
    key    = "cirgar-crawler/development/terraform.tfstate"
  }
}

