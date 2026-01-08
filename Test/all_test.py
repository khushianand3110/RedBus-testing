from Account_details.details import Account
from Bus_ticket.bus_booking import BusBooking
from Bus_ticket.passenger_details import Passengerde
from Bus_ticket.seats_points import SeatPoints
from Bus_ticket.select_bus import Selectbus
from FAQ.FAQ_Related import Related
from PNR_status.PNR import PNRstatus
from Train_ticket.train_booking import Trainbooking


def test_bus_ticket(driver):
    book = BusBooking(driver)
    book.bus_from("del")
    book.bus_to()
    book.date()
    book.for_women()
    book.search()

def test_filter_bus(driver):
    test_bus_ticket(driver)
    filter = Selectbus(driver)
    filter.filter_bus()
    filter.select_filter()
    filter.filter_2()
    filter.select_filter2()
    filter.click_bus()

def test_points_seats(driver):
    test_filter_bus(driver)
    point = SeatPoints(driver)
    point.seat_click()
    point.drop()
    point.bpoints()
    point.dpoints()


def test_train_ticket(driver):
    train = Trainbooking(driver)
    train.click_train()
    print("Click on train option")
    status = PNRstatus(driver)
    status.check_pnr()
    status.enter_pnr("1234567890")
    status.live_status("1231")

def test_my_details(driver):
    detail = Account(driver)
    detail.account_click()
    detail.bookings()
    detail.back_home()
    detail.again_account()
    detail.offers()
    detail.in_offers()

def test_details_passenger(driver):
    test_points_seats(driver)
    passenger = Passengerde(driver)
    passenger.phone_number("9786434567")
    passenger.mail_id()
    passenger.state()
    passenger.name("Priya Singh")
    passenger.age()
    passenger.genderf()
    passenger.assurance()
    passenger.protect()

def test_FAQ_related(driver):
    faq = Related(driver)
    faq.faq_section()
    faq.contents()
    faq.show_text()
    faq.popular_cities()
    faq.popular_type()



