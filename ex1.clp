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
