resource "aws_security_group" "cigar_crawler_public_subnet_all_tcp" {
  vpc_id = var.vpc_vpc_cigar_crawler_id
  name   = "cigar_crawler_public_subnet_all_tcp"

  ingress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"

    cidr_blocks = [
      var.vpc_subnet_cigar_crawler_public_a_cidr_block,
      var.vpc_subnet_cigar_crawler_public_c_cidr_block,
    ]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "cigar_crawlerpublicsubnetalltcp"
    Environment = terraform.workspace
  }
}

resource "aws_security_group" "cigar_crawler_private_subnet_all_tcp" {
  vpc_id = var.vpc_vpc_cigar_crawler_id
  name   = "cigar_crawler_private_subnet_all_tcp"

  ingress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"

    cidr_blocks = [
      var.vpc_subnet_cigar_crawler_private_a_cidr_block,
      var.vpc_subnet_cigar_crawler_private_c_cidr_block,
    ]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "cigar_crawlerprivatesubnetalltcp"
    Environment = terraform.workspace
  }
}

resource "aws_security_group" "cigar_crawler_ecs" {
  vpc_id = var.vpc_vpc_cigar_crawler_id
  name   = "cigar_crawler_ecs"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "cigar_crawlerecs"
    Environment = terraform.workspace
  }
}
