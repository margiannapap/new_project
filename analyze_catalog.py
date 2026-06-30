import numpy as np
from astropy.io import fits
import heracles as hera

print("--- Analyzing Catalog with HERACLES Context ---")

try:
    print("Loading catalog.fits safely...")
    with fits.open('catalog.fits', memmap=True) as hdul:
        data = hdul[1].data
        
        # We slice a small chunk first (e.g., first 1 million galaxies) 
        # to do a quick test without memory issues
        print("Slicing a subset for testing (1,000,000 galaxies)...")
        sub_z = data['ZTRUE'][:1000000]
        sub_e1 = data['E1'][:1000000]
        
        # Calculate some quick statistics
        mean_z = np.mean(sub_z)
        mean_e1 = np.mean(sub_e1)
        
        print("\n=== Dataset Statistics (Subset) ===")
        print(f"Mean Redshift (ZTRUE): {mean_z:.4f}")
        print(f"Mean Ellipticity (E1): {mean_e1:.4f}")
        print("\nHERACLES readiness test: Complete!")

except Exception as e:
    print(f"\n[ERROR] An error occurred: {e}")

input("\n=== PRESS ENTER TO CLOSE THIS WINDOW ===")
