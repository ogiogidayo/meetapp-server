resource "aws_ecr_repository" "api" {
  name                 = "app/ecr/${var.project}/${var.environment}"
  image_tag_mutability = "MUTABLE"
  force_delete = true

  image_scanning_configuration {
    scan_on_push = false
  }

  encryption_configuration {
    encryption_type = "KMS"
  }
}