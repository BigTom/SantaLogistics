Due to the growth in demand for gifts Santa has reorganised his workshops and delivery systems.

Gift manufacture has been outsourced to various mythical suppliers. 
 
Gift delivery is operated by Rudolf Rapid Remittance (RRR) organised by geographical region.

Santa manages the incoming requests (letters to Santa), and distributes 
gift lists for specific delivery locations) to the appropriate workshops.  
Workshops ship batches of gifts (known in the business as "Sacks") to RRR for delivery.

It is important that the RRR teams have enough reindeer kibble to make 
the trips.  Reindeer are notoriously bad with computers and, as the kibble requirement 
is dependent on the size and quantity of gifts the workshops pre-calculate the 
kibble requirement ahead of shipment so the reindeer can kibble-up without having to do
any typing.

The process is:
1. Letters to Santa arrive at Santa's Grotto
1. Santa and the polar bears create "Sack Requests" for the workshops, each sack 
 request is a list of gifts made by that workshop that will be delivered 
 to one destination (identified by capital city)
1. The sack requests are then sent to the workshops
1. For each sack request received a workshop calculates the cost of the requested sack, 
applies any discount and calculates the RRR Kibble Consumption Rate (in kibble / degree latitude travelled) 
based on the contents of the sack (number and type of gift)
1. Finally the sack's kibble requirement is calculated by multiplying KCR (in k/lat) by the number of 
degrees latitude from the north pole to the target city.  A cover note with gift count (as a check) and kibble 
requirement for the delivery are sent in a cover note with the sack

The process is currently manual and far to much time is being spent doing sums
and not enough making gifts.  Santa has decided to automate! 

The feeling is that the best place to start is the workshops because:
* The reindeer cannot use computers very well (hooves...)
* The polar bears are too frightening!

As it turns out the biggest problem in the workshops is simply calculating the basic cost of the gifts 
(who knew Trolls were so bad at counting).

Currently the workshops do have mechanical tills for adding up purchases.
The idea is to replace these with  new electronic "tills" that
will do the adding up and more.

The next biggest problem is working out the kibble requirement

Santa is feeling generous this year so he is not so worried about getting a discount but it is still a 
requirement.

An example sack request looks like this

`ELVES`\
`GIFT,COUNT`\
`TOP,10`\
`HOOP,40`\
`HULA HOOP,20`

The invoice returned to the Grotto is:
---

This is content, format is to be decided.

WORKSHOP NAME

GIFT | COUNT | Total Cost
---|---|---
TOP | 10 | ₻20.00
HOOP | 40 | ₻140.00
HULA HOOP | 20 | ₻105.00

`Total:    ₻265.00`\
`Discount:    5.0%`\
`Total:      ₻245.50`

---
(Discount is round to nearest 0.5 in favour of the workshop)


An example sack cover letter to RRR looks like this:\
`Total gifts: 70 Destination: Berlin Kibble requirement 4.147`

---
Santas currency symbol (Xmas Marks) is ₻

### You have three data files (all CSV):
##### RRR location data
`country name, capital city, latitude and longitude`

##### discounts
`total cost, discounts by workshop for cost`

##### gifts
`GIFT,WORKSHOP,COST,KIBBLE RATE/DEGREE LATITUDE`






