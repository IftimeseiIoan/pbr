(deffacts fapte
		(PrinterDoesNotPrint yes)
		(ARedLightIsFlashing no)
		(PrinterIsNotRecognised yes)
)


(defrule sit1

	(PrinterDoesNotPrint yes)
	(ARedLightIsFlashing yes)
	(PrinterIsNotRecognised yes)

	=>

	(printout t "Check the printer-computer cable  ")
	(printout t "Ensure printer software is installed  ")
	(printout t "Check/replace ink ")


)

(defrule sit2

	(PrinterDoesNotPrint yes)
	(ARedLightIsFlashing yes)
	(PrinterIsNotRecognised no)

	=>

	(printout t "Check/replace ink ")
	(printout t "Check for paper jam ")
	


)

(defrule sit3

	(PrinterDoesNotPrint yes)
	(ARedLightIsFlashing no)
	(PrinterIsNotRecognised yes)

	=>

	(printout t "Check the power cable ")
	(printout t "Check the printer-computer cable ")
	(printout t "Ensure printer software is installed ")


)

(defrule sit4

	(PrinterDoesNotPrint yes)
	(ARedLightIsFlashing no)
	(PrinterIsNotRecognised no)

	=>

	(printout t "Check for paper jam")
	

)

(defrule sit5

	(PrinterDoesNotPrint no)
	(ARedLightIsFlashing yes)
	(PrinterIsNotRecognised yes)

	=>

	(printout t "Ensure printer software is installed ")
	(printout t "Check/replace ink ")
	


)

(defrule sit6

	(PrinterDoesNotPrint no)
	(ARedLightIsFlashing yes)
	(PrinterIsNotRecognised no)

	=>

	(printout t "Check/replace ink")
	


)

(defrule sit7

	(PrinterDoesNotPrint no)
	(ARedLightIsFlashing no)
	(PrinterIsNotRecognised yes)

	=>

	(printout t "Ensure printer software is installed")
	


)

(defrule sit8

	(PrinterDoesNotPrint no)
	(ARedLightIsFlashing no)
	(PrinterIsNotRecognised no)

	=>

	(printout t " ")
	


)

