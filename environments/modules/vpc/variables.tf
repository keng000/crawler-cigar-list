variable "availability_zone" {
  default = {
    "production.a" = "ap-northeast-1a"
    "production.c" = "ap-northeast-1c"
    "development.a" = "ap-northeast-2a"
    "development.c" = "ap-northeast-2c"
  }
}
