import astropy.io.fits as fits
import matplotlib.pyplot as plt

print("--- Loading FIRST 50,000 Objects Only ---")

try:
    hdul = fits.open("../catalog.fits")
    ra_sample = hdul[1].data['RA'][:50000]
    dec_sample = hdul[1].data['DEC'][:50000]
    hdul.close()

    print("Generating plot...")
    plt.figure(figsize=(8, 5))
    plt.scatter(ra_sample, dec_sample, s=0.1, color="blue", alpha=0.5)
    
    plt.title("Galaxy Catalog Distribution")
    plt.xlabel("Right Ascension (RA)")
    plt.ylabel("Declination (DEC)")
    plt.grid(True, linestyle="--", alpha=0.7)

    # Αποθήκευση σε αρχείο εικόνας
    print("Saving plot as 'my_galaxy_plot.png'...")
    plt.savefig("my_galaxy_plot.png", dpi=150)
    print("SUCCESS! File saved. You can close the terminal now.")

except Exception as e:
    print(f"\n[ERROR]: {e}")
