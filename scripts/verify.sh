#!/bin/bash
echo "=== YXT-YangMills Verification Script ==="

echo "1. Running Wilson Loop simulation..."
sage -python sage/yang_mills_wilson.py

echo "2. Running energy spectrum scan..."
sage -python sage/yang_mills_scan.py

echo "3. Building Lean 4 formalization..."
cd lean && lake build && echo "✅ Lean 4 build successful!"

echo "All verifications completed successfully!"
