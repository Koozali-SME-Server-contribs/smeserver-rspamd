# Enable milter mode for Postfix integration
milter = yes;
timeout = 120s;
upstream "local" {
  default = yes;
  self_scan = yes;  # Scan messages directly
}
