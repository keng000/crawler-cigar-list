provider "aws" {
  version = "~> 2.5"
  region  = lookup(var.region, terraform.workspace)
}
