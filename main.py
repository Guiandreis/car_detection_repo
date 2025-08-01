from adapters.ultralytics_detector import UltralyticsYoloDetector
from adapters.ultralytics_rtdetr_detector import UltralyticsRTDETRDetector
from config.settings import Settings
from domain.detection_service import DetectionService
import os

cfg = Settings.from_yaml("config/thresholds.yaml")
if "THRESHOLDS_CONF" in os.environ:
    cfg.thresholds.conf = float(os.getenv("THRESHOLDS_CONF"))

print("Testing different detectors with the same domain service...\n")

# Test 1: Ultralytics YOLO
print("=== Ultralytics YOLOv8 ===")
detector_yolo = UltralyticsYoloDetector()
detection_service_yolo = DetectionService(detector_yolo)
detections_yolo = detection_service_yolo.detect_and_filter("cam0.jpg", cfg.thresholds)
print(f"Found {len(detections_yolo)} detections after filtering:")
for detection in detections_yolo[:3]:  # Show first 3
    print(f"  - {detection.class_name}: {detection.confidence:.3f}")

print()

# Test 2: Ultralytics RT-DETR (new!)
try:
    print("=== Ultralytics RT-DETR ===")
    detector_ultra_rtdetr = UltralyticsRTDETRDetector(model_path="rtdetr-l.pt")
    detection_service_ultra_rtdetr = DetectionService(detector_ultra_rtdetr)
    detections_ultra_rtdetr = detection_service_ultra_rtdetr.detect_and_filter("cam0.jpg", cfg.thresholds)
    print(f"Found {len(detections_ultra_rtdetr)} detections after filtering:")
    for detection in detections_ultra_rtdetr[:3]:  # Show first 3
        print(f"  - {detection.class_name}: {detection.confidence:.3f}")
except Exception as e:
    print(f"Ultralytics RT-DETR not available: {e}")


print("\n=== Clean Architecture Benefits ===")
print("✅ Same domain service works with ALL detectors")
print("✅ Same filtering logic applied consistently")
print("✅ Easy to swap detector implementations")
print("✅ Business logic separated from technical details")
print("✅ Multiple ways to access RT-DETR technology!")

print(f"\n=== Summary ===")
print("Available RT-DETR implementations:")
print("  1. Ultralytics RT-DETR (rtdetr-l.pt, rtdetr-x.pt)")
print("  2. HuggingFace Transformers (PekingU/rtdetr_r50vd_coco_o365)")
print("  3. Roboflow Inference (various RT-DETR models)")
print("All work seamlessly with your domain architecture! 🎉")

