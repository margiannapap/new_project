import numpy as np
from astropy.io import fits

print("--- Safely Inspecting FITS Dataset ---")

try:
    print("Opening catalog.fits with memory mapping...")
    with fits.open('catalog.fits', memmap=True) as hdul:
        print("\n=== FITS File Structure ===")
        hdul.info()
        
        if len(hdul) > 1:
            data_summary = hdul[1]
            print("\n=== Data Extension Details ===")
            print(f"Total rows (objects): {len(data_summary.data)}")
            print("\nAvailable columns in this dataset:")
            print(data_summary.columns.names)
            print("\nPreview of the first 3 rows:")
            print(data_summary.data[:3])
        else:
            print("\n[Warning] This FITS file only contains the primary HDU.")

except FileNotFoundError:
    print("\n[ERROR] Could not find 'catalog.fits' in this directory.")
except Exception as e:
    print(f"\n[ERROR] An unexpected error occurred: {e}")

input("\n=== PRESS ENTER TO CLOSE THIS WINDOW ===")
