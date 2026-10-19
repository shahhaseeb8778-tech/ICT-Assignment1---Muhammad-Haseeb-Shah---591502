# C5.py  Star-Delta Transformation: converts Star (Y) network to Delta network

def star_to_delta(star_ra, star_rb, star_rc):
    numerator = (star_ra * star_rb) + (star_rb * star_rc) + (star_rc * star_ra)
    delta_rab = numerator / star_rc
    delta_rbc = numerator / star_ra
    delta_rca = numerator / star_rb
    return (round(delta_rab, 2), round(delta_rbc, 2), round(delta_rca, 2))
result = star_to_delta(10, 20, 30)
print(f"star_to_delta(10, 20, 30) -> {result}")
result2= star_to_delta(5,10,15)
print(f"star_to_delta(5,10,15)->{result2}")