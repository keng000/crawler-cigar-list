resource "aws_ecr_repository" "crawler" {
  name = "cigar-crawler/crawler"
}

resource "aws_ecr_lifecycle_policy" "crawler" {
  repository = "${aws_ecr_repository.crawler.name}"

  policy = "${file("${path.module}/policy.json")}"
}
