resource "aws_ecs_cluster" "cigar_crawler_cluster" {
  name = "cigar_crawler"

  tags = {
    Name        = "cigar_crawler"
    Environment = terraform.workspace
  }
}
