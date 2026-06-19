import numpy as np
from astropy.io import fits

print("--- Running Tomographic Bin Analysis ---")

try:
    print("Opening catalog.fits safely...")
    with fits.open('catalog.fits', memmap=True) as hdul:
        data = hdul[1].data
        
        # 1. Find unique tomographic bins
        print("Analyzing tomographic bins...")
        unique_bins = np.unique(data['BIN'])
        print(f"Detected Tomographic Bins: {unique_bins}")
        
        print("\n=== Bin Distribution & Statistics ===")
        print(f"{'Bin ID':<10}{'Galaxy Count':<15}{'Mean Redshift (ZTRUE)':<25}")
        print("-" * 50)
        
        # 2. Loop through each bin to calculate statistics safely
        for b in unique_bins:
            # Masking to select only galaxies belonging to the current bin
            bin_mask = (data['BIN'] == b)
            
            # Count galaxies in this bin
            count = np.sum(bin_mask)
            
            # Calculate mean redshift for this specific bin
            mean_z = np.mean(data['ZTRUE'][bin_mask])
            
            print(f"{b:<10}{count:<15,}{mean_z:.4f}")
            
        print("\nTomographic analysis completed successfully!")

except Exception as e:
    print(f"\n[ERROR] An error occurred: {e}")

input("\n=== PRESS ENTER TO CLOSE THIS WINDOW ===")
