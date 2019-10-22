# VPC Settings
resource "aws_vpc" "cigar_crawler" {
  cidr_block = "10.1.0.0/16"

  enable_dns_hostnames = true
  enable_dns_support   = true
  enable_classiclink   = false

  instance_tenancy = "default"

  tags = {
    Name        = "cigar_crawler"
    Environment = terraform.workspace
    Workspace   = terraform.workspace
  }
}

# Public Subnets Settings
resource "aws_subnet" "cigar_crawler_public_a" {
  vpc_id            = aws_vpc.cigar_crawler.id
  cidr_block        = "10.1.1.0/24"
  availability_zone = lookup(var.availability_zone, "${terraform.workspace}.a")

  tags = {
    Name        = "cigar_crawler_public_a"
    Environment = terraform.workspace
    Workspace   = terraform.workspace
  }
}

resource "aws_subnet" "cigar_crawler_public_c" {
  vpc_id            = aws_vpc.cigar_crawler.id
  cidr_block        = "10.1.3.0/24"
  availability_zone = lookup(var.availability_zone, "${terraform.workspace}.c")

  tags = {
    Name        = "cigar_crawler_public_c"
    Environment = terraform.workspace
    Workspace   = terraform.workspace
  }
}

# Private Subnets Settings
resource "aws_subnet" "cigar_crawler_private_a" {
  vpc_id            = aws_vpc.cigar_crawler.id
  cidr_block        = "10.1.100.0/24"
  availability_zone = lookup(var.availability_zone, "${terraform.workspace}.a")

  tags = {
    Name        = "cigar_crawler_private_a"
    Environment = terraform.workspace
    Workspace   = terraform.workspace
  }
}

resource "aws_subnet" "cigar_crawler_private_c" {
  vpc_id            = aws_vpc.cigar_crawler.id
  cidr_block        = "10.1.101.0/24"
  availability_zone = lookup(var.availability_zone, "${terraform.workspace}.c")

  tags = {
    Name        = "cigar_crawler_private_c"
    Environment = terraform.workspace
    Workspace   = terraform.workspace
  }
}

# Routes Table Settings
resource "aws_route_table" "cigar_crawler-public-rt" {
  vpc_id = aws_vpc.cigar_crawler.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.cigar_crawler-igw.id
  }

  tags = {
    Name        = "cigar_crawler_public_rt"
    Environment = terraform.workspace
    Workspace   = terraform.workspace
  }
}

resource "aws_route_table_association" "cigar_crawler-rta1" {
  subnet_id      = aws_subnet.cigar_crawler_public_a.id
  route_table_id = aws_route_table.cigar_crawler-public-rt.id
}

resource "aws_route_table_association" "cigar_crawler-rta2" {
  subnet_id      = aws_subnet.cigar_crawler_public_c.id
  route_table_id = aws_route_table.cigar_crawler-public-rt.id
}

# DHCP option sets
resource "aws_vpc_dhcp_options" "cigar_crawler-dhcp" {
  domain_name_servers = ["AmazonProvidedDNS"]

  tags = {
    Name        = "cigar_crawler_dhcp"
    Environment = terraform.workspace
    Workspace   = terraform.workspace
  }
}

resource "aws_vpc_dhcp_options_association" "cigar_crawler-dhcp-association" {
  vpc_id          = aws_vpc.cigar_crawler.id
  dhcp_options_id = aws_vpc_dhcp_options.cigar_crawler-dhcp.id
}

# Internet Gateway Settings
resource "aws_internet_gateway" "cigar_crawler-igw" {
  vpc_id = aws_vpc.cigar_crawler.id

  tags = {
    Name        = "cigar_crawler_igw"
    Environment = terraform.workspace
    Workspace   = terraform.workspace
  }
}
